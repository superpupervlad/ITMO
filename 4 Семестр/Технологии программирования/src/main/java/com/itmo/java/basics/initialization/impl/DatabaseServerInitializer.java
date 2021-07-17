package com.itmo.java.basics.initialization.impl;

import com.itmo.java.basics.console.ExecutionEnvironment;
import com.itmo.java.basics.exceptions.DatabaseException;
import com.itmo.java.basics.initialization.InitializationContext;
import com.itmo.java.basics.initialization.Initializer;
import com.itmo.java.basics.initialization.InitializerHelper;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class DatabaseServerInitializer extends InitializerHelper implements Initializer {

    public DatabaseServerInitializer(DatabaseInitializer databaseInitializer) {
        childInitializer = databaseInitializer;
    }

    /**
     * Если заданная в окружении директория не существует - создает ее
     * Добавляет информацию о существующих в директории базах, начинает их инициализацию
     *
     * @param context контекст, содержащий информацию об окружении
     * @throws DatabaseException если произошла ошибка при создании директории, ее обходе или ошибка инициализации бд
     */
    @Override
    public void perform(InitializationContext context) throws DatabaseException {
        ExecutionEnvironment execEnv = context.executionEnvironment();
        Path workingPath = execEnv.getWorkingPath();

        if (!workingPath.toFile().isDirectory()) {
            try {
                Files.createDirectory(workingPath);
            } catch (IOException e) {
                throw new DatabaseException("Can't create directory for Database: " + "\n" +
                        "Working path: " + workingPath + e);
            }
        }
        iterateOverDirectoriesAndPerformChild(context, workingPath);
    }

    @Override
    protected InitializationContext createChildContext(InitializationContext context, File currentFile) {
        return InitializationContextImpl.builder()
                .executionEnvironment(context.executionEnvironment())
                .currentDatabaseContext(
                        new DatabaseInitializationContextImpl(currentFile.getName(), currentFile.toPath().getParent()))
                .build();
    }
}
