package com.itmo.java.basics.console;

import com.itmo.java.basics.logic.Database;

import java.nio.file.Path;
import java.util.Optional;

public interface ExecutionEnvironment {
    /**
     * @return путь до директории, где находятся базы данных
     */
    Path getWorkingPath();

    /**
     * Возвращает {@code Optional<Database>} или {@code Optional#EMPTY}.
     *
     * @param name имя базы данных
     * @return {@code Optional<Database>}
     */
    Optional<Database> getDatabase(String name);

    /**
     * Добавляет базу данных в текущее окружение.
     *
     * @param db база данных, которую нужно добавить
     */
    void addDatabase(Database db);
}
