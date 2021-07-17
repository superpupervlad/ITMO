package com.itmo.java.basics.initialization.impl;

import com.itmo.java.basics.exceptions.DatabaseException;
import com.itmo.java.basics.index.impl.SegmentOffsetInfoImpl;
import com.itmo.java.basics.initialization.InitializationContext;
import com.itmo.java.basics.initialization.Initializer;
import com.itmo.java.basics.initialization.SegmentInitializationContext;
import com.itmo.java.basics.logic.DatabaseRecord;
import com.itmo.java.basics.logic.Segment;
import com.itmo.java.basics.logic.impl.SegmentImpl;
import com.itmo.java.basics.logic.io.DatabaseInputStream;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Optional;

public class SegmentInitializer implements Initializer {

    /**
     * Добавляет в контекст информацию об инициализируемом сегменте.
     * Составляет индекс сегмента
     * Обновляет инфу в индексе таблицы
     *
     * @param context контекст с информацией об инициализируемой бд и об окружении
     * @throws DatabaseException если в контексте лежит неправильный путь к сегменту, невозможно прочитать содержимое. Ошибка в содержании
     */
    @Override
    public void perform(InitializationContext context) throws DatabaseException {
        SegmentInitializationContext segmentContext = context.currentSegmentContext();
        File file = segmentContext.getSegmentPath().toFile();
        var index = segmentContext.getIndex();

        if (!file.exists()) {
            throw new DatabaseException("Segment file doesn't exist" + "\n" +
                    "Path: " + file.getPath());
        }

        try (DatabaseInputStream inputStream = new DatabaseInputStream(new FileInputStream(file))) {
            int offsetCount = 0;
            while (inputStream.available() != 0) {
                Optional<DatabaseRecord> dbRecord = inputStream.readDbUnit();
                index.onIndexedEntityUpdated(new String(dbRecord.get().getKey()), new SegmentOffsetInfoImpl(offsetCount));
                offsetCount += dbRecord.get().size();
            }

            Segment segment = SegmentImpl.initializeFromContext(
                    new SegmentInitializationContextImpl(
                        segmentContext.getSegmentName(),
                        segmentContext.getSegmentPath(),
                        offsetCount,
                        segmentContext.getIndex()));

            context.currentTableContext().updateCurrentSegment(segment);
            context.currentTableContext().getTableIndex().updateMultipleEntitiesWithOneValue(index, segment);
        } catch (IOException e) {
            throw new DatabaseException("Error while reading file: " + "\n" +
                    "File: " + file.getPath(), e);
        }
    }
}
