package com.itmo.java.protocol.model;

import java.io.IOException;
import java.io.OutputStream;
import java.nio.charset.StandardCharsets;
import java.util.List;

/**
 * Массив RESP объектов
 */
public class RespArray implements RespObject {
    private final RespObject[] objects;

    /**
     * Код объекта
     */
    public static final byte CODE = '*';

    public RespArray(RespObject... objects) {
        this.objects = objects;
    }

    /**
     * Ошибка ли это? Ответ - нет
     *
     * @return false
     */
    @Override
    public boolean isError() {
        return false;
    }

    /**
     * Строковое представление
     *
     * @return результаты метода {@link RespObject#asString()} для всех хранимых объектов, разделенные пробелом
     */
    @Override
    // TODO Добавлять строку в кеш чтобы не формировать 1000 раз?
    public String asString() {
        StringBuilder concatenatedStringsBuffer = new StringBuilder();
        for (RespObject respObject: objects) {
            concatenatedStringsBuffer.append(respObject.asString());
            concatenatedStringsBuffer.append(' ');
        }

        return concatenatedStringsBuffer.toString();
    }

    @Override
    public void write(OutputStream os) throws IOException {
        os.write(CODE);
        os.write(String.valueOf(objects.length).getBytes(StandardCharsets.UTF_8));
        os.write(CRLF);

        for (RespObject respObject: objects) {
            respObject.write(os);
        }
    }

    public List<RespObject> getObjects() {
        return List.of(objects);
    }
}
