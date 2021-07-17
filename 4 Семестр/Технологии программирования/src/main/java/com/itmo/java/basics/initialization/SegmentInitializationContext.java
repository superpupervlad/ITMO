package com.itmo.java.basics.initialization;

import com.itmo.java.basics.index.impl.SegmentIndex;

import java.nio.file.Path;

public interface SegmentInitializationContext {
    /**
     * Возвращает имя инициализируемого сегмента.
     *
     * @return имя инициализируемого сегмента
     */
    String getSegmentName();

    /**
     * Возвращает путь до файла сегмента.
     *
     * @return путь до файла сегмента
     */
    Path getSegmentPath();

    /**
     * Возвращает индекс инициализируемого сегмента.
     *
     * @return индекс инициализируемого сегмента
     */
    SegmentIndex getIndex();

    /**
     * Возвращает текущий размер инициализируемого сегмента.
     *
     * @return текущий размер инициализируемого сегмента
     */
    long getCurrentSize();
}
