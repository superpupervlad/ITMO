package com.itmo.java.basics.config;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

// TODO подсказку бы что нужно юзать java.util.Properties
/**
 * Класс, отвечающий за подгрузку данных из конфигурационного файла формата .properties
 */
public class ConfigLoader {
    private String configName;

    // static чтобы можно было передавать в конструктор
    private static final String DEFAULT_CONFIG_NAME = "server.properties";
    private final Properties DEFAULT_PROPERTIES = new Properties();

    /**
     * По умолчанию читает из server.properties
     */
    public ConfigLoader() {
        this(DEFAULT_CONFIG_NAME);
    }

    /**
     * @param name Имя конфикурационного файла, откуда читать
     */
    public ConfigLoader(String name) {
        configName = name;

        DEFAULT_PROPERTIES.setProperty("kvs.workingPath", DatabaseConfig.DEFAULT_WORKING_PATH);
        DEFAULT_PROPERTIES.setProperty("kvs.host", ServerConfig.DEFAULT_HOST);
        DEFAULT_PROPERTIES.setProperty("kvs.port", String.valueOf(ServerConfig.DEFAULT_PORT));
    }

    /**
     * Считывает конфиг из указанного в конструкторе файла.
     * Если не удалось считать из заданного файла, или какого-то конкретно значения не оказалось,
     * то используют дефолтные значения из {@link DatabaseConfig} и {@link ServerConfig}
     * <br/>
     * Читаются: "kvs.workingPath", "kvs.host", "kvs.port" (но в конфигурационном файле допустимы и другие проперти)
     */
    public DatabaseServerConfig readConfig() {
        Properties prop = new Properties(DEFAULT_PROPERTIES);
        InputStream input;

        input = this.getClass().getClassLoader().getResourceAsStream(configName);
        if (input == null) {
            try {
                input = new FileInputStream(configName);
            } catch (FileNotFoundException ignored) {
            }
        }

        try {
            prop.load(input);
        } catch (IOException | NullPointerException ignored) {
        }

        return new DatabaseServerConfig(
            new ServerConfig(
                prop.getProperty("kvs.host"),
                Integer.parseInt(prop.getProperty("kvs.port"))),
            new DatabaseConfig(
                prop.getProperty("kvs.workingPath")
            )
        );
    }
}
