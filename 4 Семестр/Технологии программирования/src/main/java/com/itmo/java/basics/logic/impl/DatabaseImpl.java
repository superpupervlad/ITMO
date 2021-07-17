package com.itmo.java.basics.logic.impl;

import com.itmo.java.basics.exceptions.DatabaseException;
import com.itmo.java.basics.index.impl.TableIndex;
import com.itmo.java.basics.initialization.DatabaseInitializationContext;
import com.itmo.java.basics.logic.Database;
import com.itmo.java.basics.logic.Table;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashMap;
import java.util.Map;
import java.util.Optional;

public class DatabaseImpl implements Database {
    private final String databaseName;
    private Path databaseRoot;
    private final Path selfDirectory;
    private Map<String, Table> tables = new HashMap<>();

    /**
     * @param databaseRoot путь к директории, которая может содержать несколько БД,
     *                     поэтому при создании БД необходимо создать директорию внутри databaseRoot.
     */
    public static Database create(String dbName, Path databaseRoot) throws DatabaseException {
        if (dbName.isEmpty()) {
            throw new DatabaseException("Name of database is null -__-");
        }

        DatabaseImpl db = new DatabaseImpl(
                dbName,
                databaseRoot.resolve(dbName),
                databaseRoot);

        try {
            Files.createDirectory(db.selfDirectory);
        } catch (IOException e) {
            throw new DatabaseException("Failed to create database! " + "\n" +
                    "Name: " + dbName + "\n" +
                    "Path: " + databaseRoot + e);
        }

        return db;
    }

	public static Database initializeFromContext(DatabaseInitializationContext context) {
        return new DatabaseImpl(
                context.getDbName(),
                context.getDatabasePath(),
                context.getTables());
    }

    private DatabaseImpl(String databaseName, Path selfDirectory, Map<String, Table> tables) {
        this.databaseName = databaseName;
        this.selfDirectory = selfDirectory;
        this.tables = tables;
    }

    private DatabaseImpl(String databaseName, Path selfDirectory, Path databaseRoot) {
        this.databaseName = databaseName;
        this.selfDirectory = selfDirectory;
        this.databaseRoot = databaseRoot;
    }

    @Override
    public String getName() {
        return databaseName;
    }

    @Override
    public void createTableIfNotExists(String tableName) throws DatabaseException {
        if (tables.containsKey(tableName)) {
            throw new DatabaseException("Table with this name already exist (" + tableName + ")");
        }

        tables.put(tableName, TableImpl.create(tableName, selfDirectory, new TableIndex()));
    }

    @Override
    public void write(String tableName, String objectKey, byte[] objectValue) throws DatabaseException {
        if (tables.containsKey(tableName)) {
            tables.get(tableName).write(objectKey, objectValue);
        }
        else {
            throw new DatabaseException("Can't write: No such table (" + tableName + ")");
        }
    }

    @Override
    public Optional<byte[]> read(String tableName, String objectKey) throws DatabaseException {
        if (tables.containsKey(tableName)) {
            return tables.get(tableName).read(objectKey);
        }
        else {
            throw new DatabaseException("Can't read: No such table (" + tableName + ")");
        }
    }

    @Override
    public void delete(String tableName, String objectKey) throws DatabaseException {
        if (tables.containsKey(tableName)) {
            tables.get(tableName).delete(objectKey);
        }
        else {
            throw new DatabaseException("Can't delete: No such table (" + tableName + ")");
        }
    }
}
