package com.itmo.java.basics.console;

// TODO почему это здесь, а не в пакете protocol?
/**
 * Описывает порядок аргументов.
 * Например, используется для парсинга следующих конструкций: "1 CREATE_DATABASE db1" или "1 SET_KEY db1 table1 key"
 */
public enum DatabaseCommandArgPositions {
    COMMAND_ID(0),
    COMMAND_NAME(1),
    DATABASE_NAME(2),
    TABLE_NAME(3),
    KEY(4),
    VALUE(5);

    private final int positionIndex;

    DatabaseCommandArgPositions(int positionIndex) {
        this.positionIndex = positionIndex;
    }

    public int getPositionIndex() {
        return positionIndex;
    }
}