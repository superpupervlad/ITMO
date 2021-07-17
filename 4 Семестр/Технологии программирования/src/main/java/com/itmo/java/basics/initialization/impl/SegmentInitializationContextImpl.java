package com.itmo.java.basics.initialization.impl;

import com.itmo.java.basics.index.impl.SegmentIndex;
import com.itmo.java.basics.initialization.SegmentInitializationContext;

import java.nio.file.Path;

public class SegmentInitializationContextImpl implements SegmentInitializationContext {
    private String segmentName;
    private Path segmentPath;
    private long currentSize;
    private SegmentIndex index;

    public SegmentInitializationContextImpl(String segmentName, Path segmentPath, long currentSize, SegmentIndex index) {
        this.segmentName = segmentName;
        this.segmentPath = segmentPath;
        this.currentSize = currentSize;
        this.index = index;
    }

    /**
     *        (•_•)                     (•_•)
     *        (ง )ง                     ୧( ୧)
     *        /︶\                      /︶\
     * Не используйте этот     Не используйте эти тесты.
     * конструктор. Оставлен
     * для совместимости со
     * старыми тестами.
     */
    public SegmentInitializationContextImpl(String segmentName, Path tablePath, long currentSize) {
        this(segmentName,
            tablePath.resolve(segmentName),
            currentSize,
            new SegmentIndex());
    }

    public SegmentInitializationContextImpl(String segmentName, Path tablePath) {
        this(segmentName, tablePath.resolve(segmentName), 0, new SegmentIndex());
    }

    @Override
    public String getSegmentName() {
        return segmentName;
    }

    @Override
    public Path getSegmentPath() {
        return segmentPath;
    }

    @Override
    public SegmentIndex getIndex() {
        return index;
    }

    @Override
    public long getCurrentSize() {
        return currentSize;
    }
}
