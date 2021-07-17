package com.itmo.java.protocol.model;

import java.io.IOException;
import java.io.OutputStream;
import java.nio.charset.StandardCharsets;

/**
 * Строка
 */
public class RespBulkString implements RespObject {
    byte[] data;

    /**
     * Код объекта
     */
    public static final byte CODE = '$';

    public static final int NULL_STRING_SIZE = -1;

    public static final RespBulkString NULL_STRING = new RespBulkString(null);

    public RespBulkString(byte[] data) {
        this.data = data;
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
     * @return строку, если данные есть. Если нет - null
     */
    @Override
    public String asString() {
        // Вы можете заставить нас ставить скобки в однострочных if, но вы забыли про тернарные операторы.
        return (data == null || data.length == 0) ? null : new String(data);
    }

    @Override
    public void write(OutputStream os) throws IOException {
        if (data != null) {
            os.write(CODE);
            os.write(String.valueOf(data.length).getBytes(StandardCharsets.UTF_8));
            os.write(CRLF);
            os.write(data);
            os.write(CRLF);
        }
        else {
            os.write(CODE);
            os.write(String.valueOf(NULL_STRING_SIZE).getBytes(StandardCharsets.UTF_8));
            os.write(CRLF);
        }
    }
}
