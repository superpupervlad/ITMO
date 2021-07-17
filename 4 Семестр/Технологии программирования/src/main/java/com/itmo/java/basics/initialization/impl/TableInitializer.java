package com.itmo.java.basics.initialization.impl;

import com.itmo.java.basics.exceptions.DatabaseException;
import com.itmo.java.basics.initialization.InitializationContext;
import com.itmo.java.basics.initialization.Initializer;
import com.itmo.java.basics.initialization.InitializerHelper;
import com.itmo.java.basics.initialization.IterableOverFiles;
import com.itmo.java.basics.logic.impl.TableImpl;

import java.io.File;
import java.nio.file.Path;
import java.util.Arrays;

public class TableInitializer extends InitializerHelper implements Initializer, IterableOverFiles {

    public TableInitializer(SegmentInitializer segmentInitializer) {
        childInitializer = segmentInitializer;
    }

    /**
     * Добавляет в контекст информацию об инициализируемой таблице.
     * Запускает инициализацию всех сегментов в порядке их создания (из имени)
     *
     * @param context контекст с информацией об инициализируемой бд, окружении, таблицы
     * @throws DatabaseException если в контексте лежит неправильный путь к таблице, невозможно прочитать содержимого папки,
     *                           или если возникла ошибка ошибка дочерних инициализаторов
     */
    @Override
    public void perform(InitializationContext context) throws DatabaseException {
        iterateOverFilesAndPerformChild(context, context.currentTableContext().getTablePath());
        context.currentDbContext().addTable(TableImpl.initializeFromContext(context.currentTableContext()));
    }

    @Override
    public void iterateOverFilesAndPerformChild(InitializationContext context, Path currentWorkingPath) throws DatabaseException {
        checkIfDirectoryExistElseThrowException(currentWorkingPath);

        var files = currentWorkingPath.toFile().listFiles();
        if (files != null) {
            Arrays.sort(files);

            for (File inode : files) {
                if (inode.isFile()) {
                    childInitializer.perform(createChildContext(context, inode));
                }
            }
        }
    }

    @Override
    protected InitializationContext createChildContext(InitializationContext context, File currentFile) {
        return InitializationContextImpl.builder()
                .executionEnvironment(context.executionEnvironment())
                .currentDatabaseContext(context.currentDbContext())
                .currentTableContext(context.currentTableContext())
                .currentSegmentContext(
                        new SegmentInitializationContextImpl(currentFile.getName(), context.currentTableContext().getTablePath()))
                .build();
    }

}
