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
 * Команда для создания базы таблицы
 */
public class CreateTableCommand extends CommandHelper implements DatabaseCommand {
    private final String CORRECT_COMMAND_NAME = "CREATE_TABLE";
    private final short CORRECT_NUMBER_OF_ARGUMENTS = 4;

    /**
     * Создает команду
     * <br/>
     * Обратите внимание, что в конструкторе нет логики проверки валидности данных. Не проверяется, можно ли исполнить команду. Только формальные признаки (например, количество переданных значений или ненуловость объектов
     *
     * @param env         env
     * @param commandArgs аргументы для создания (порядок - {@link DatabaseCommandArgPositions}.
     *                    Id команды, имя команды, имя бд, имя таблицы
     * @throws IllegalArgumentException если передано неправильное количество аргументов
     */
    public CreateTableCommand(ExecutionEnvironment env, List<RespObject> commandArgs) {
        checkArgs(commandArgs, CORRECT_COMMAND_NAME, CORRECT_NUMBER_OF_ARGUMENTS);

        this.env = env;
        this.commandArgs = commandArgs;
    }

    /**
     * Создает таблицу в нужной бд
     *
     * @return {@link DatabaseCommandResult#success(byte[])} с сообщением о том, что заданная таблица была создана. Например, "Table table1 in database db1 created"
     */
    @Override
    public DatabaseCommandResult execute() {
        // я.извиняюсь.как().дико.но(это.пи(дец)).ifNotNull().toString().exclamationMark()
        String tableName = commandArgs.get(DatabaseCommandArgPositions.TABLE_NAME.getPositionIndex()).asString();
        String dbName = commandArgs.get(DatabaseCommandArgPositions.DATABASE_NAME.getPositionIndex()).asString();

        Optional<Database> db = env.getDatabase(dbName);
        if (db.isPresent()) {
            try {
                db.get().createTableIfNotExists(tableName);
            } catch (DatabaseException e) {
                return DatabaseCommandResult.error(e);
            }
        }
        else {
            return DatabaseCommandResult.error("Can't create table!\nDatabase with this name doesn't exist!");
        }

        return new SuccessDatabaseCommandResult(("Table " + tableName + " in " + dbName + " successfully created").getBytes());
    }
}
