package com.itmo.java.basics.initialization;

import com.itmo.java.basics.logic.Table;

import java.nio.file.Path;
import java.util.Map;

public interface DatabaseInitializationContext {
    /**
     * Возвращает имя инициализируемой базы данных.
     *
     * @return имя инициализируемой базы данных
     */
    String getDbName();

    /**
     * Возвращает путь до директории инициализируемой базы данных.
     *
     * @return путь до директории инициализируемой базы данных
     */
    Path getDatabasePath();

    /**
     * Возвращает ассоциативный массив таблиц, который накопился на данном этапе инициализации.
     *
     * @return массив таблиц, который накопился на данном этапе инициализации
     */
    Map<String, Table> getTables();

    /**
     * Добавляет таблицу в ассоциативный массив накопленных таблиц.
     *
     * @throws RuntimeException если указанная таблица уже добавлена
     * @param table таблица, которую нужно добавить
     */
    void addTable(Table table);
}