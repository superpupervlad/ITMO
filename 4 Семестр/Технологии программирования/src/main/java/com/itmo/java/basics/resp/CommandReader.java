package com.itmo.java.basics.resp;

import com.itmo.java.basics.console.DatabaseCommand;
import com.itmo.java.basics.console.DatabaseCommandArgPositions;
import com.itmo.java.basics.console.DatabaseCommands;
import com.itmo.java.basics.console.ExecutionEnvironment;
import com.itmo.java.protocol.RespReader;
import com.itmo.java.protocol.model.RespArray;

import java.io.IOException;
// TODO почему если есть RReader и RWriter, то нет CommandWriter
public class CommandReader implements AutoCloseable {
    private final ExecutionEnvironment env;
    private final RespReader reader;

    public CommandReader(RespReader reader, ExecutionEnvironment env) {
        this.env = env;
        this.reader = reader;
    }

    /**
     * Есть ли следующая команда в ридере?
     */
    public boolean hasNextCommand() throws IOException {
        return reader.hasArray();
    }

    /**
     * Считывает команду с помощью ридера и возвращает ее
     *
     * @throws IllegalArgumentException если нет имени команды и id
     */
    public DatabaseCommand readCommand() throws IOException {
        RespArray command = reader.readArray();
        try {
            return DatabaseCommands
                    .valueOf(command.getObjects().get(DatabaseCommandArgPositions.COMMAND_NAME.getPositionIndex()).asString())
                    .getCommand(env, command.getObjects());
        }
        catch (ArrayIndexOutOfBoundsException e) {
            throw new IllegalArgumentException(e);
        }
    }

    @Override
    public void close() throws Exception {
        reader.close();
    }
}
