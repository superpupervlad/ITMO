package com.itmo.java.basics.console;

public interface DatabaseCommand {
    /**
     * Запускает команду.
     *
     * @return Сообщение о выполнении результата команды.
     */
    DatabaseCommandResult execute();
}
