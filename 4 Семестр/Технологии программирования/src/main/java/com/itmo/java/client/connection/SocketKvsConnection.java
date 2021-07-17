package com.itmo.java.client.connection;

import com.itmo.java.client.exception.ConnectionException;
import com.itmo.java.protocol.RespReader;
import com.itmo.java.protocol.RespWriter;
import com.itmo.java.protocol.model.RespArray;
import com.itmo.java.protocol.model.RespObject;

import java.io.IOException;
import java.net.Socket;

/**
 * С помощью {@link RespWriter} и {@link RespReader} читает/пишет в сокет
 */
public class SocketKvsConnection implements KvsConnection {
    private final String host;
    private final int port;
    private final Socket socket;
    private final RespReader reader;
    private final RespWriter writer;

    public SocketKvsConnection(ConnectionConfig config) {
        this.host = config.getHost();
        this.port = config.getPort();
        try {
            this.socket = new Socket(host, port);
            this.writer = new RespWriter(socket.getOutputStream());
            this.reader = new RespReader(socket.getInputStream());
        } catch (IOException e) {
            throw new RuntimeException("Can't create connection", e);
        }
    }

    /**
     * Отправляет с помощью сокета команду и получает результат.
     * @param commandId id команды (номер)
     * @param command   команда
     * @throws ConnectionException если сокет закрыт или если произошла другая ошибка соединения
     */
    @Override
    public synchronized RespObject send(int commandId, RespArray command) throws ConnectionException {
        try {
            writer.write(command);
            return reader.readObject();
        } catch (Exception e) {
            throw new ConnectionException("Error occurred while sending command: " + command.asString(), e);
        }
    }

    /**
     * Закрывает сокет (и другие использованные ресурсы)
     */
    @Override
    public void close() {
        // 12/10
        try {
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        try {
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

        try {
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
