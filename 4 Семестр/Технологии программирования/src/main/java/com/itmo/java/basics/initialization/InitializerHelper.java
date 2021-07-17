package com.itmo.java.basics.initialization;

import com.itmo.java.basics.exceptions.DatabaseException;

import java.io.File;
import java.nio.file.Path;
import java.util.Arrays;

public abstract class InitializerHelper {
    public Initializer childInitializer;

    public void checkIfDirectoryExistElseThrowException (Path path) throws DatabaseException {
        if (!path.toFile().isDirectory()) {
            throw new DatabaseException("Directory doesn't exist" + " " +
                    "Path: " + path);
        }
    }

    public void iterateOverDirectoriesAndPerformChild (InitializationContext context, Path currentWorkingPath) throws DatabaseException {
        checkIfDirectoryExistElseThrowException(currentWorkingPath);

        var directories = currentWorkingPath.toFile().listFiles();
        if (directories != null) {
            Arrays.sort(directories);

            for (File file : directories) {
                if (file.isDirectory()) {
                    childInitializer.perform(createChildContext(context, file));
                }
            }
        }
    }

    protected abstract InitializationContext createChildContext (InitializationContext context, File currentFile) throws DatabaseException;
}
