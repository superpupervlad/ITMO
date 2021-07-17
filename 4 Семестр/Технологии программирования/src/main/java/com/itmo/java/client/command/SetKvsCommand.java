package com.itmo.java.client.command;

import com.itmo.java.protocol.model.RespArray;
import com.itmo.java.protocol.model.RespBulkString;
import com.itmo.java.protocol.model.RespCommandId;

public class SetKvsCommand extends CommandIdIncrementable implements KvsCommand {
    String databaseName;
    String tableName;
    String key;
    String value;

    private static final String COMMAND_NAME = "SET_KEY";

    public SetKvsCommand(String databaseName, String tableName, String key, String value) {
        this.databaseName = databaseName;
        this.tableName = tableName;
        this.key = key;
        this.value = value;
    }

    /**
     * Возвращает RESP объект. {@link RespArray} с {@link RespCommandId}, именем команды, аргументами в виде {@link RespBulkString}
     *
     * @return объект
     */
    @Override
    public RespArray serialize() {
        return new RespArray(
                    new RespCommandId(getCommandId()),
                    new RespBulkString(COMMAND_NAME.getBytes()),
                    new RespBulkString(databaseName.getBytes()),
                    new RespBulkString(tableName.getBytes()),
                    new RespBulkString(key.getBytes()),
                    new RespBulkString(value.getBytes())
        );
    }
}
