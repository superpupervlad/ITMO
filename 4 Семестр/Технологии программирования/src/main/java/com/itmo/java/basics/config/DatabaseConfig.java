package com.itmo.java.basics.config;

public class DatabaseConfig {
    public static final String DEFAULT_WORKING_PATH = "db_files";
    private final String path;

    public DatabaseConfig(String workingPath) {
        if (workingPath.isEmpty()) {
            path = DEFAULT_WORKING_PATH;
        } else {
            path = workingPath;
        }
    }

    public String getWorkingPath() {
        return path;
    }
}
