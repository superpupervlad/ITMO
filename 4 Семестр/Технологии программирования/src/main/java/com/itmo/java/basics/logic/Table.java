package com.itmo.java.basics.logic;

import com.itmo.java.basics.exceptions.DatabaseException;

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
public interface Table {
    /**
     * Возвращает имя таблицы.
     *
     * @return имя таблицы
     */
    String getName();

    /**
     * Записывает в таблицу переданное значение по указанному ключу.
     *
     * @param objectKey ключ, по которому нужно записать значение
     * @param objectValue значение, которое нужно записать
     * @throws DatabaseException если произошла ошибка ввода-вывода
     */
    void write(String objectKey, byte[] objectValue) throws DatabaseException;

    /**
     * Считывает значение из таблицы по заданному ключу.
     *
     * @param objectKey ключ, по которому нужно получить значение
     * @return значение, которое находится по ключу
     * @throws DatabaseException если произошла ошибка ввода-вывода
     */
    Optional<byte[]> read(String objectKey) throws DatabaseException;

    void delete(String objectKey) throws DatabaseException;
}

