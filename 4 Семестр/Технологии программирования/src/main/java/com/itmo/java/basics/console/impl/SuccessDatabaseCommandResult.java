package com.itmo.java.basics.console.impl;

import com.itmo.java.basics.console.DatabaseCommandResult;
import com.itmo.java.protocol.model.RespBulkString;
import com.itmo.java.protocol.model.RespObject;

/**
 * Результат успешной команды
 */
public class SuccessDatabaseCommandResult implements DatabaseCommandResult {
    byte[] payload;

    public SuccessDatabaseCommandResult(byte[] payload) {
        this.payload = payload;
    }

    @Override
    public String getPayLoad() {
        return (payload == null || payload.length == 0) ? null : new String(payload);
    }

    @Override
    public boolean isSuccess() {
        return true;
    }

    /**
     * Сериализуется в {@link RespBulkString}
     */
    @Override
    public RespObject serialize() {
        return new RespBulkString(payload);
    }
}
