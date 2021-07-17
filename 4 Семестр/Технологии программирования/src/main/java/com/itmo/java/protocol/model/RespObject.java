package com.itmo.java.protocol.model;

import java.io.IOException;
import java.io.OutputStream;
import java.nio.charset.StandardCharsets;

/**
 * Представляет собой объект в RESP
 */
public interface RespObject {

    /**
     * Последовательность символов, означающая конец объекта
     */
    byte[] CRLF = "\r\n".getBytes(StandardCharsets.UTF_8);

    /**
     * @return {@code true} - если данный объект представляет ошибку, {@code false} - в ином случае
     */
    boolean isError();

    /**
     * @return возвращает строковое значение команды (не в RESP, без специальных символов).
     * Например, для {@link RespBulkString} со значением "string" - "string"
     */
    String asString();

    /**
     * Сериализует данный объект в RESP и записывает байты в переданный OutputStream.
     */
    void write(OutputStream os) throws IOException;
}