package com.itmo.java.client.exception;

/**
 * Ошибка подключения
 */
public class ConnectionException extends Exception {
    public ConnectionException(String message) {
        super(message);
    }

    public ConnectionException(String message, Throwable cause) {
        super(message, cause);
    }
}
