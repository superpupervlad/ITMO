package com.itmo.java.client.connection;

import lombok.AllArgsConstructor;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.ToString;

/**
 * Класс содержит информацию, что слушает сервер, по какому адресу с ним взаимодействовать.
 * (По идее они должны совпадать с тем, какие мы используем в server.properties)
 */
@Getter
@ToString
@EqualsAndHashCode
@AllArgsConstructor
public class ConnectionConfig {
    public static final String DEFAULT_HOST = "localhost";
    public static final int DEFAULT_PORT = 8080;

    private final String host;
    private final int port;
}