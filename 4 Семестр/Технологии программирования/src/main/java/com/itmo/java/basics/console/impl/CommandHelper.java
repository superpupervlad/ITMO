package com.itmo.java.basics.console.impl;

import com.itmo.java.basics.console.ExecutionEnvironment;
import com.itmo.java.protocol.model.RespObject;

import java.util.List;

public abstract class CommandHelper {
    ExecutionEnvironment env;
    List<RespObject> commandArgs;

    protected void checkArgs(List<RespObject> commandArgs, String correctCommandName, short correctNumberOfArgs) throws IllegalArgumentException {
        if (commandArgs.size() != correctNumberOfArgs // ||
                // TODO проходит без проверки на правильное имя
                // в теории мы можем случайно передать запрос от клиента на получение ключа, в DeleteKeyCommand
                // проверить на кол-во аргументов и по ошибке удалить ключ
//                !commandArgs.get(DatabaseCommandArgPositions.COMMAND_NAME.getPositionIndex()).asString().equals(correctCommandName) ||
//                commandArgs.stream().anyMatch(Objects::isNull)
        ) {
            StringBuilder arguments = new StringBuilder();
            for (RespObject argument : commandArgs) {
                arguments.append(argument);
                arguments.append('\n');
            }
            throw new IllegalArgumentException("Wrong format of command arguments!" + "\n" +
                    "Given arguments:" + "\n" +
                    arguments.toString());
        }
    }
}