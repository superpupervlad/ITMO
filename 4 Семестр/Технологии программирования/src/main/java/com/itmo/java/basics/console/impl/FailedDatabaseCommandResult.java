package com.itmo.java.basics.console.impl;

import com.itmo.java.basics.console.DatabaseCommandResult;
import com.itmo.java.protocol.model.RespError;
import com.itmo.java.protocol.model.RespObject;

/**
 * Зафейленная команда
 */
public class FailedDatabaseCommandResult implements DatabaseCommandResult {
    String payload;

    // TODO почему здесь String, а в success byte[]
    public FailedDatabaseCommandResult(String payload) {
        this.payload = payload;
    }

    /**
     * Сообщение об ошибке
     */
    @Override
    public String getPayLoad() {
        return payload;
    }

    // TODO зачем когда можно проверять isInstance?
    //  А лучше вообще сделать только один класс и хранить успех/неудачу как поле
    @Override
    public boolean isSuccess() {
        return false;
    }

    /**
     * Сериализуется в {@link RespError}
     */
    @Override
    public RespObject serialize() {
        return new RespError(payload.getBytes());
    }
}
