package com.itmo.java.basics.console;

import com.itmo.java.basics.console.impl.FailedDatabaseCommandResult;
import com.itmo.java.basics.console.impl.SuccessDatabaseCommandResult;
import com.itmo.java.protocol.model.RespObject;

public interface DatabaseCommandResult extends DatabaseApiSerializable {

    /**
     * Формирует успешный результат выполнения команды из значения результата.
     *
     * @param result значение результата
     * @return успешный результат выполнения команды, который был сформирован
     */
    static DatabaseCommandResult success(byte[] result) {
        return new SuccessDatabaseCommandResult(result);
    }

    /**
     * Формирует зафейленный результат команды, при выполнении которой произошла ошибка.
     *
     * @param message сообщение об ошибке
     * @return результат зафейленный команды, при выполнении которой произошла ошибка
     */
    static DatabaseCommandResult error(String message) {
        return new FailedDatabaseCommandResult(message);
    }

    /**
     * Формирует результат команды, при выполнении которой произошла ошибка.
     * Берется сообщение из исключения. Если в исключении нет сообщения - стэктрейс
     *
     * @param exception исключение, из которого нужно сформировать результат выполнения команды
     * @return результат команды, при выполнении которой произошла ошибка
     */
    static DatabaseCommandResult error(Exception exception) {
        // TODO нужно ли так проверять
        if (exception.getMessage().isBlank() || exception.getMessage() == null) {
            return new FailedDatabaseCommandResult(String.valueOf(exception.getStackTrace()));
        }
        else {
            return new FailedDatabaseCommandResult(exception.getMessage());
        }
    }

    /**
     * @return значение результата выполнения команды в виде {@code Optional<String>}
     */
    String getPayLoad();

    /**
     * @return {@code true} - если команда выполнилась успешно, {@code false} - в ином случае
     */
    boolean isSuccess();


    @Override
    RespObject serialize();
}