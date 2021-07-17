package com.itmo.java.client.command;

import com.itmo.java.protocol.model.RespArray;
import com.itmo.java.protocol.model.RespBulkString;
import com.itmo.java.protocol.model.RespCommandId;

/**
 * Команда для создания таблицы
 */
public class CreateTableKvsCommand extends CommandIdIncrementable implements KvsCommand {
    String databaseName;
    String tableName;

    private static final String COMMAND_NAME = "CREATE_TABLE";

    public CreateTableKvsCommand(String databaseName, String tableName) {
        this.databaseName = databaseName;
        this.tableName = tableName;
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
                new RespBulkString(tableName.getBytes())
        );
    }
}
