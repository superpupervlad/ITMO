package com.itmo.java.basics.logic.impl;

import com.itmo.java.basics.exceptions.DatabaseException;
import com.itmo.java.basics.index.impl.TableIndex;
import com.itmo.java.basics.logic.Segment;
import com.itmo.java.basics.initialization.TableInitializationContext;
import com.itmo.java.basics.logic.Table;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.Optional;

/**
 * Таблица - логическая сущность, представляющая собой набор файлов-сегментов, которые объединены одним
 * именем и используются для хранения однотипных данных (данных, представляющих собой одну и ту же сущность,
 * например, таблица "Пользователи")
 * <p>
 * - имеет единый размер сегмента
 * - представляет из себя директорию в файловой системе, именованную как таблица
 * и хранящую файлы-сегменты данной таблицы
 */
public class TableImpl implements Table {
    private final String name;
    private final TableIndex index;
    private final Path selfDirectory;
    private Segment currentSegment;

    // TODO Почему здесь передаем tableindex, а в Segment нет, а?
    public static Table create(String tableName, Path pathToDatabaseRoot, TableIndex tableIndex) throws DatabaseException {
        if (tableName.isEmpty()) {
            throw new DatabaseException("Name is null -__- ");
        }

        TableImpl table = new TableImpl(
                pathToDatabaseRoot.resolve(tableName),
                tableIndex,
                tableName);

        try {
            Files.createDirectory(table.selfDirectory);
        } catch (IOException e) {
            throw new DatabaseException("Failed to create table" + "\n" +
                    "Name: " + tableName + "\n" +
                    "Database path: " + pathToDatabaseRoot, e);
        }

        return new CachingTable(table);
    }

    public static Table initializeFromContext(TableInitializationContext context) {
        return new CachingTable(
                new TableImpl(
                        context.getTablePath(),
                        context.getTableIndex(),
                        context.getTableName(),
                        context.getCurrentSegment()));
    }

    private TableImpl(Path selfDirectory, TableIndex index, String name) {
        this.selfDirectory = selfDirectory;
        this.index = index;
        this.name = name;
    }

    private TableImpl(Path selfDirectory, TableIndex index, String name, Segment segment) {
        this(selfDirectory, index, name);
        this.currentSegment = segment;
    }

    private void addNewSegment() throws DatabaseException {
        currentSegment = SegmentImpl.create(SegmentImpl.createSegmentName(name), selfDirectory);
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public void write(String objectKey, byte[] objectValue) throws DatabaseException {
        if (currentSegment == null || currentSegment.isReadOnly()) {
            addNewSegment();
        }

        index.onIndexedEntityUpdated(objectKey, currentSegment);

        try {
            currentSegment.write(objectKey, objectValue);
        } catch (IOException e) {
            throw new DatabaseException("Can't write to segment" + "\n" +
                    "Key: " + objectKey + "\n" +
                    "Value: " + Arrays.toString(objectValue), e);
        }
    }

    @Override
    public Optional<byte[]> read(String objectKey) throws DatabaseException {
        try {
            Optional<Segment> segment = index.searchForKey(objectKey);
            if (segment.isPresent()) {
                return segment.get().read(objectKey);
            } else {
                return Optional.empty();
            }
        } catch (IOException e) {
            throw new DatabaseException("Can't read from segment" + "\n" +
                    "Key: " + objectKey + e);
        }
    }

    @Override
    public void delete(String objectKey) throws DatabaseException {
        Optional<Segment> segment = index.searchForKey(objectKey);
        if (segment.isPresent()) {
            try {
                if (currentSegment == null || currentSegment.isReadOnly()) {
                    addNewSegment();
                }
                currentSegment.delete(objectKey);
                index.onIndexedEntityUpdated(objectKey, currentSegment);
            } catch (IOException e) {
                throw new DatabaseException("Can't delete key" + "\n" +
                        "Key: " + objectKey, e);
            }
        } else throw new DatabaseException("Can't delete key: no such key (" + objectKey + ")");
    }
}
