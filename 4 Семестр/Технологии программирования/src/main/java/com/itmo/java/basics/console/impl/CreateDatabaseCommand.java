package com.itmo.java.basics.console.impl;

import com.itmo.java.basics.console.DatabaseCommand;
import com.itmo.java.basics.console.DatabaseCommandArgPositions;
import com.itmo.java.basics.console.DatabaseCommandResult;
import com.itmo.java.basics.console.ExecutionEnvironment;
import com.itmo.java.basics.exceptions.DatabaseException;
import com.itmo.java.basics.logic.DatabaseFactory;
import com.itmo.java.protocol.model.RespObject;

import java.util.List;

// TODO сначала extends или implements?
/**
 * Команда для создания базы данных
 */
public class CreateDatabaseCommand extends CommandHelper implements DatabaseCommand {
    DatabaseFactory factory;

    // TODO правильное расположение (порядок) полей в классе
    private final String CORRECT_COMMAND_NAME = "CREATE_DATABASE";
    private final short CORRECT_NUMBER_OF_ARGUMENTS = 3;

    /**
     * Создает команду.
     * <br/>
     * Обратите внимание, что в конструкторе нет логики проверки валидности данных. Не проверяется, можно ли исполнить команду. Только формальные признаки (например, количество переданных значений или ненуловость объектов
     *
     * @param env         env
     * @param factory     функция создания базы данных (пример: DatabaseImpl::create)
     * @param commandArgs аргументы для создания (порядок - {@link DatabaseCommandArgPositions}.
     *                    Id команды, имя команды, имя создаваемой бд
     * @throws IllegalArgumentException если передано неправильное количество аргументов
     */
    public CreateDatabaseCommand(ExecutionEnvironment env, DatabaseFactory factory, List<RespObject> commandArgs) {
        // TODO Нужно ли писать в заголовок об ошибках???
        checkArgs(commandArgs, CORRECT_COMMAND_NAME, CORRECT_NUMBER_OF_ARGUMENTS);

        this.commandArgs = commandArgs;
        this.env = env;
        this.factory = factory;
    }

    /**
     * Создает бд в нужном env
     *
     * @return {@link DatabaseCommandResult#success(byte[])} с сообщением о том, что заданная база была создана. Например, "Database db1 created"
     */
    @Override
    public DatabaseCommandResult execute() {
        String dbName = commandArgs.get(DatabaseCommandArgPositions.DATABASE_NAME.getPositionIndex()).asString();

        try {
            env.addDatabase(factory.createNonExistent(dbName, env.getWorkingPath()));
        } catch (DatabaseException e) {
            return DatabaseCommandResult.error(e);
        }

        return DatabaseCommandResult.success(("Database " + dbName + " in " + env.getWorkingPath() + " successfully created").getBytes());
    }
}
