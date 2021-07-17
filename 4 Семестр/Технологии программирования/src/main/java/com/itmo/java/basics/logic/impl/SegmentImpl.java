package com.itmo.java.basics.logic.impl;

import com.itmo.java.basics.exceptions.DatabaseException;
import com.itmo.java.basics.index.SegmentOffsetInfo;
import com.itmo.java.basics.index.impl.SegmentIndex;
import com.itmo.java.basics.index.impl.SegmentOffsetInfoImpl;
import com.itmo.java.basics.initialization.SegmentInitializationContext;
import com.itmo.java.basics.logic.DatabaseRecord;
import com.itmo.java.basics.logic.Segment;
import com.itmo.java.basics.logic.io.DatabaseInputStream;
import com.itmo.java.basics.logic.io.DatabaseOutputStream;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Optional;

/**
 * Сегмент - append-only файл, хранящий пары ключ-значение, разделенные специальным символом.
 * - имеет ограниченный размер, большие значения (>100000) записываются в последний сегмент, если он не read-only
 * - при превышении размера сегмента создается новый сегмент и дальнейшие операции записи производятся в него
 * - именование файла-сегмента должно позволять установить очередность их появления
 * - является неизменяемым после появления более нового сегмента
 */
public class SegmentImpl implements Segment {
    private final String name;
    private final Path tablePath;
    private File file;
    private final SegmentIndex index;
    private long currentOffset;
    private final int MAX_SIZE = 100_000;

    public static Segment create(String segmentName, Path tableRootPath) throws DatabaseException {
        SegmentImpl segment = new SegmentImpl(segmentName, tableRootPath, new SegmentIndex());

        try {
            segment.file = Files.createFile(tableRootPath.resolve(segmentName)).toFile();
        } catch (IOException e) {
            throw new DatabaseException("Can't create segment file" + "\n" +
                    "Name: " + segmentName + " " +
                    "Table path: " + tableRootPath, e);
        }

        return segment;
    }

    private SegmentImpl(String name, Path tablePath, SegmentIndex index) {
        this.name = name;
        this.tablePath = tablePath;
        this.index = index;
        this.currentOffset = 0;
    }

    private SegmentImpl(String name, Path tablePath, SegmentIndex index, File file, long currentOffset) {
        this(name, tablePath, index);
        this.file = file;
        this.currentOffset = currentOffset;
    }

    public static Segment initializeFromContext(SegmentInitializationContext context) {
        return new SegmentImpl(
                context.getSegmentName(),
                context.getSegmentPath().getParent(),
                context.getIndex(),
                context.getSegmentPath().toFile(),
                context.getCurrentSize());
    }

    static String createSegmentName(String tableName) {
        return tableName + "_" + System.currentTimeMillis();
    }

    public SegmentIndex getIndex() {
        return index;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public boolean write(String objectKey, byte[] objectValue) throws IOException {
        if (isReadOnly()) {
            return false;
        }

        index.onIndexedEntityUpdated(objectKey, new SegmentOffsetInfoImpl(currentOffset));

        try (DatabaseOutputStream outputStream = new DatabaseOutputStream(new FileOutputStream(file, true))) {
            currentOffset += outputStream.write(new SetDatabaseRecord(objectKey, objectValue));
        } catch (IOException e) {
            throw new IOException("Can't create output stream" + "\n" +
                    "Name: " + name + "\n" +
                    "Table path: " + tablePath.toString(), e);
        }

        return true;
    }

    @Override
    public Optional<byte[]> read(String objectKey) throws IOException {
        Optional<SegmentOffsetInfo> offsetInfo = index.searchForKey(objectKey);
        if (offsetInfo.isEmpty()) {
            return Optional.empty();
        }

        try (DatabaseInputStream inputStream = new DatabaseInputStream(new FileInputStream(file))) {
            long offset = offsetInfo.get().getOffset();
            if (offset != inputStream.skip(offset)) {
                throw new IOException("Skipped wrong amount of bytes" + "\n" +
                        "File: " + file.getName() + "\n" +
                        "Key: " + objectKey);
            }

            Optional<DatabaseRecord> dbRecord = inputStream.readDbUnit();
            if (dbRecord.isPresent() && dbRecord.get().isValuePresented()) {
                return Optional.of(dbRecord.get().getValue());
            } else {
                return Optional.empty();
            }
        } catch (IOException e) {
            throw new IOException("Can't create input stream" + "\n" +
                    "Name: " + name + "\n" +
                    "Table path: " + tablePath.toString(), e);
        }
    }

    @Override
    public boolean isReadOnly() {
        return currentOffset >= MAX_SIZE;
    }

    @Override
    public boolean delete(String objectKey) throws IOException {
        if (isReadOnly()) {
            return false;
        }

        index.onIndexedEntityUpdated(objectKey, new SegmentOffsetInfoImpl(currentOffset));

        try (DatabaseOutputStream outputStream = new DatabaseOutputStream(new FileOutputStream(file, true))) {
            currentOffset = outputStream.write(new RemoveDatabaseRecord(objectKey));
        } catch (IOException e) {
            throw new IOException("Can't create output stream" + "\n" +
                    "Name: " + name + "\n" +
                    "Table path: " + tablePath.toString(), e);
        }

        return true;
    }
}
