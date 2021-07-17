package com.itmo.java.client.command;

import com.itmo.java.protocol.model.RespArray;

import java.util.concurrent.atomic.AtomicInteger;

public interface KvsCommand {
    // TODO нужно бы указать, что это связано с RespCommandId, а то не совсем очевидно
    /**
     * Счетчик для команды. Каждая созданная команда использует это поле для создания id, инкрементирует значение
     * Первая команда создается с id 0
     */
    AtomicInteger idGen = new AtomicInteger();

    /**
     * Сериализует объект в RESP
     *
     * @return RESP объект
     */
    RespArray serialize();

    /**
     * Id команды
     *
     * @return id
     */
    int getCommandId();
}
