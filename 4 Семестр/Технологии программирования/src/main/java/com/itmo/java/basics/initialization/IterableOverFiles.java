package com.itmo.java.basics.initialization;

import com.itmo.java.basics.exceptions.DatabaseException;

import java.nio.file.Path;

public interface IterableOverFiles {
    void iterateOverFilesAndPerformChild(InitializationContext context, Path currentWorkingPath) throws DatabaseException;
}
