package com.itmo.java.basics.connector;

import com.itmo.java.basics.DatabaseServer;
import com.itmo.java.basics.config.ServerConfig;
import com.itmo.java.basics.console.DatabaseCommandResult;
import com.itmo.java.basics.resp.CommandReader;
import com.itmo.java.protocol.RespReader;
import com.itmo.java.protocol.RespWriter;

import java.io.Closeable;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/**
 * Класс, который предоставляет доступ к серверу через сокеты
 */
public class JavaSocketServerConnector implements Closeable {
    DatabaseServer databaseServer;
    ServerConfig config;

    /**
     * Экзекьютор для выполнения ClientTask
     */
    private final ExecutorService clientIOWorkers = Executors.newSingleThreadExecutor();

    private final ServerSocket serverSocket;
    private final ExecutorService connectionAcceptorExecutor = Executors.newSingleThreadExecutor();

    /**
     * Стартует сервер. По аналогии с сокетом открывает коннекшн в конструкторе.
     */
    public JavaSocketServerConnector(DatabaseServer databaseServer, ServerConfig config) throws IOException {
        this.serverSocket = new ServerSocket(config.getPort());
        this.databaseServer = databaseServer;
        this.config = config;
    }

    /**
     * Начинает слушать заданный порт, начинает аксептить клиентские сокеты. На каждый из них начинает клиентскую таску
     */
    public void start() {
        connectionAcceptorExecutor.submit(() -> {
            while (!Thread.currentThread().isInterrupted()) {
                try {
                    Socket newClientConnection = serverSocket.accept();
                    clientIOWorkers.submit(new ClientTask(newClientConnection, databaseServer));
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
    }

    /**
     * Закрывает все, что нужно ¯\_(ツ)_/¯
     */
    @Override
    public void close() {
        System.out.println("Stopping socket connector");
        clientIOWorkers.shutdownNow();
        connectionAcceptorExecutor.shutdownNow();
        try {
            serverSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) throws Exception {
        // можно запускать прямо здесь
    }

    /**
     * Runnable, описывающий исполнение клиентской команды.
     */
    static class ClientTask implements Runnable, Closeable {
        private final Socket client;
        private final DatabaseServer server;
        private final CommandReader commandReader;
        private final RespWriter respWriter;

        /**
         * @param client клиентский сокет
         * @param server сервер, на котором исполняется задача
         */
        public ClientTask(Socket client, DatabaseServer server) {
            this.client = client;
            this.server = server;
            try {
                this.commandReader = new CommandReader(new RespReader(client.getInputStream()), server.getEnv());
                this.respWriter = new RespWriter(client.getOutputStream());
            } catch (IOException e) {
                throw new RuntimeException("Can't create ClientTask", e);
            }
        }

        // TODO так красивше
        /**
         * Исполняет задачи из одного клиентского сокета, пока клиент не отсоединился или текущий поток не был прерван (interrupted).
         * Для каждой из задач:
         * <ol>
         *   <li>Читает из сокета команду с помощью {@link CommandReader}</li>
         *   <li>Исполняет ее на сервере</li>
         *   <li>Записывает результат в сокет с помощью {@link RespWriter}</li>
         * </ol>
         */
        @Override
        public void run() {
            try {
                while (commandReader.hasNextCommand()) {
                    DatabaseCommandResult result;
                    try {
                        result = server.executeNextCommand(commandReader.readCommand()).get();
                    } catch (IllegalArgumentException e) {
                        result = DatabaseCommandResult.error(e);
                    }
                    respWriter.write(result.serialize());
                }
            }
            catch (Exception ignored) {
            } finally {
                close();
            }
        }

        /**
         * Закрывает клиентский сокет
         */
        @Override
        public void close() {
            try {
                commandReader.close();
            } catch (Exception e) {
                e.printStackTrace();
            }

            try {
                client.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
