package com.itmo.java.basics.initialization.impl;

import com.itmo.java.basics.exceptions.DatabaseException;
import com.itmo.java.basics.index.impl.TableIndex;
import com.itmo.java.basics.initialization.InitializationContext;
import com.itmo.java.basics.initialization.Initializer;
import com.itmo.java.basics.initialization.InitializerHelper;
import com.itmo.java.basics.logic.impl.DatabaseImpl;

import java.io.File;
import java.nio.file.Path;

public class DatabaseInitializer extends InitializerHelper implements Initializer {

    public DatabaseInitializer(TableInitializer tableInitializer) {
        childInitializer = tableInitializer;
    }

    /**
     * Добавляет в контекст информацию об инициализируемой бд.
     * Запускает инициализацию всех таблиц этой базы
     *
     * @param initialContext контекст с информацией об инициализируемой бд и об окружении
     * @throws DatabaseException если в контексте лежит неправильный путь к базе, невозможно прочитать содержимого папки,
     *  или если возникла ошибка дочерних инициализаторов
     */
    @Override
    public void perform(InitializationContext initialContext) throws DatabaseException {
        iterateOverDirectoriesAndPerformChild(initialContext, initialContext.currentDbContext().getDatabasePath());
        initialContext.executionEnvironment()
                .addDatabase(DatabaseImpl.initializeFromContext(initialContext.currentDbContext()));
    }

    @Override
    protected InitializationContext createChildContext(InitializationContext context, File currentFile) {
        return InitializationContextImpl.builder()
                .executionEnvironment(context.executionEnvironment())
                .currentDatabaseContext(context.currentDbContext())
                .currentTableContext(
                        new TableInitializationContextImpl(currentFile.getName(), Path.of(currentFile.getParent()), new TableIndex()))
                .build();
    }
}
