package com.itmo.java.client.command;

// Можно было бы это сделать и в изначальном интерфейсе, но тогда не будут проходить тесты.
// А еще можно объединить все эти классы в один.
// Ctrl-C + Ctrl-V для полей, для конструктора, для метода 👍👍👍
public abstract class CommandIdIncrementable implements KvsCommand {
    int commandId = -1;

    @Override
    public int getCommandId() {
        if (commandId == -1) {
            commandId = idGen.getAndAdd(1);
        }

        return commandId;
    }
}
