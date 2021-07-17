package com.itmo.java.client.connection;

import com.itmo.java.client.exception.ConnectionException;
import com.itmo.java.protocol.model.RespArray;
import com.itmo.java.protocol.model.RespObject;

/**
 * Определяет интерфейс подключения к key value storage
 */
public interface KvsConnection extends AutoCloseable {
    /**
     * Отправляет команду к серверу
     *
     * @param commandId id команды (номер)
     * @param command   команда
     * @return Результат исполнения
     * @throws ConnectionException если не удалось прочитать ответ
     */
    RespObject send(int commandId, RespArray command) throws ConnectionException;
}
