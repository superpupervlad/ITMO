package com.itmo.java.basics.console.impl;

import com.itmo.java.basics.console.DatabaseCommand;
import com.itmo.java.basics.console.DatabaseCommandArgPositions;
import com.itmo.java.basics.console.DatabaseCommandResult;
import com.itmo.java.basics.console.ExecutionEnvironment;
import com.itmo.java.basics.exceptions.DatabaseException;
import com.itmo.java.basics.logic.Database;
import com.itmo.java.protocol.model.RespObject;

import java.util.List;
import java.util.Optional;

/**
 * Команда для чтения данных по ключу
 */
public class GetKeyCommand extends CommandHelper implements DatabaseCommand {
    private final String CORRECT_COMMAND_NAME = "GET_KEY";
    private final short CORRECT_NUMBER_OF_ARGUMENTS = 5;

    /**
     * Создает команду.
     * <br/>
     * Обратите внимание, что в конструкторе нет логики проверки валидности данных. Не проверяется, можно ли исполнить команду. Только формальные признаки (например, количество переданных значений или ненуловость объектов
     *
     * @param env         env
     * @param commandArgs аргументы для создания (порядок - {@link DatabaseCommandArgPositions}.
     *                    Id команды, имя команды, имя бд, таблицы, ключ
     * @throws IllegalArgumentException если передано неправильное количество аргументов
     */
    public GetKeyCommand(ExecutionEnvironment env, List<RespObject> commandArgs) {
        checkArgs(commandArgs, CORRECT_COMMAND_NAME, CORRECT_NUMBER_OF_ARGUMENTS);

        this.env = env;
        this.commandArgs = commandArgs;
    }

    /**
     * Читает значение по ключу
     *
     * @return {@link DatabaseCommandResult#success(byte[])} с прочитанным значением. Например, "previous". Null, если такого нет
     */
    @Override
    public DatabaseCommandResult execute() {
        String key = commandArgs.get(DatabaseCommandArgPositions.KEY.getPositionIndex()).asString();
        String tableName = commandArgs.get(DatabaseCommandArgPositions.TABLE_NAME.getPositionIndex()).asString();
        String dbName = commandArgs.get(DatabaseCommandArgPositions.DATABASE_NAME.getPositionIndex()).asString();

        Optional<Database> db = env.getDatabase(dbName);
        if (db.isPresent()) {
            try {
                Optional<byte[]> result = db.get().read(tableName, key);
                return DatabaseCommandResult.success(result.orElse(null));
            } catch (DatabaseException e) {
                return DatabaseCommandResult.error(e);
            }
        }
        else {
            return DatabaseCommandResult.error("Can't get value!\nDatabase with this name doesn't exist!");
        }
    }
}
