package com.itmo.java.basics.initialization;

import com.itmo.java.basics.index.impl.TableIndex;
import com.itmo.java.basics.logic.Segment;

import java.nio.file.Path;

public interface TableInitializationContext {
    /**
     * Возвращает имя инициализируемой таблицы.
     *
     * @return имя инициализируемой таблицы
     */
    String getTableName();

    /**
     * Возвращает путь до директории таблицы.
     *
     * @return путь до директории таблицы
     */
    Path getTablePath();

    /**
     * Возвращает индекс инициализируемой таблицы.
     *
     * @return индекс инициализируемой таблицы
     */
    TableIndex getTableIndex();

    /**
     * Возвращает текущий активный сегмент для инициализируемой таблицы.
     *
     * @return текущий активный сегмент для инициализируемой таблицы
     */
    Segment getCurrentSegment();

    /**
     * Обновляет текущий активный сегмент.
     *
     * @param segment новый сегмент
     */
    void updateCurrentSegment(Segment segment);
}
