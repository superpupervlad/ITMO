package com.itmo.java.basics.logic;

import java.io.IOException;
import java.util.Optional;

/**
 * Сегмент - append-only файл, хранящий пары ключ-значение, разделенные специальным символом.
 * - имеет ограниченный размер, большие значения (>100000) записываются в последний сегмент, если он не read-only
 * - при превышении размера сегмента создается новый сегмент и дальнейшие операции записи производятся в него
 * - именование файла-сегмента должно позволять установить очередность их появления
 * - является неизменяемым после появления более нового сегмента
 */
public interface Segment {
    /**
     * Возвращает имя сегмента.
     *
     * @return имя сегмента
     */
    String getName();

    /**
     * Записывает значение по указанному ключу в сегмент.
     *
     * @param objectKey ключ, по которому нужно записать значение
     * @param objectValue значение, которое нужно записать
     * @return {@code true} - если значение записалось, {@code false} - если нет
     * @throws IOException если произошла ошибка ввода-вывода.
     */
    boolean write(String objectKey, byte[] objectValue) throws IOException;

    /**
     * Считывает значение из сегмента по переданному ключу.
     *
     * @param objectKey ключ, по которому нужно получить значение
     * @return значение, которое находится по ключу
     * @throws IOException если произошла ошибка ввода-вывода
     */
    Optional<byte[]> read(String objectKey) throws IOException;

    /**
     * Возвращает {@code true} - если данный сегмент открыт только на чтение, {@code false} - если данный сегмент открыт на чтение и запись.
     *
     * @return {@code true} - если данный сегмент открыт только на чтение, {@code false} - если данный сегмент открыт на чтение и запись
     */
    boolean isReadOnly();

    boolean delete(String objectKey) throws IOException;
}