package com.itmo.java.client.client;

import com.itmo.java.client.command.CreateDatabaseKvsCommand;
import com.itmo.java.client.command.CreateTableKvsCommand;
import com.itmo.java.client.command.DeleteKvsCommand;
import com.itmo.java.client.command.GetKvsCommand;
import com.itmo.java.client.command.KvsCommand;
import com.itmo.java.client.command.SetKvsCommand;
import com.itmo.java.client.connection.KvsConnection;
import com.itmo.java.client.exception.ConnectionException;
import com.itmo.java.client.exception.DatabaseExecutionException;
import com.itmo.java.protocol.model.RespObject;

import java.util.function.Supplier;

public class SimpleKvsClient implements KvsClient {
    private final String databaseName;
    private final Supplier<KvsConnection> connectionSupplier;

    /**
     * Конструктор
     *
     * @param databaseName       имя базы, с которой работает
     * @param connectionSupplier метод создания подключения к базе
     */
    public SimpleKvsClient(String databaseName, Supplier<KvsConnection> connectionSupplier) {
        this.databaseName = databaseName;
        this.connectionSupplier = connectionSupplier;
    }

    @Override
    public String createDatabase() throws DatabaseExecutionException {
        CreateDatabaseKvsCommand command = new CreateDatabaseKvsCommand(databaseName);
        return universalCommandSender(command, "Can't create database!");
    }

    @Override
    public String createTable(String tableName) throws DatabaseExecutionException {
        CreateTableKvsCommand command = new CreateTableKvsCommand(databaseName, tableName);
        return universalCommandSender(command, "Can't create table!");
    }

    @Override
    public String get(String tableName, String key) throws DatabaseExecutionException {
        GetKvsCommand command = new GetKvsCommand(databaseName, tableName, key);
        return universalCommandSender(command, "Can't get value!");
    }

    @Override
    public String set(String tableName, String key, String value) throws DatabaseExecutionException {
        SetKvsCommand command = new SetKvsCommand(databaseName, tableName, key, value);
        return universalCommandSender(command, "Can't set value!");
    }

    @Override
    public String delete(String tableName, String key) throws DatabaseExecutionException {
        DeleteKvsCommand command = new DeleteKvsCommand(databaseName, tableName, key);
        return universalCommandSender(command, "Can't delete value!");
    }

    private String universalCommandSender(KvsCommand command, String errorMessage) throws DatabaseExecutionException {
        try {
            KvsConnection connection = connectionSupplier.get();
            RespObject serverResponse = connection.send(
                    command.getCommandId(),
                    command.serialize());
            if (serverResponse.isError()) {
                throw new DatabaseExecutionException("Server return error" + '\n' +
                        serverResponse.asString());
            }
            return serverResponse.asString();
        } catch (ConnectionException e) {
            throw new DatabaseExecutionException("Can't connect to server!", e);
        } catch (Exception e) {
            throw new DatabaseExecutionException(errorMessage, e);
        }
    }
}
