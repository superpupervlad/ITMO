package com.itmo.java.basics.logic.io;

import com.itmo.java.basics.logic.WritableDatabaseRecord;
import com.itmo.java.basics.logic.impl.RemoveDatabaseRecord;

import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStream;

/**
 * Записывает данные в БД
 */
public class DatabaseOutputStream extends DataOutputStream {

    public DatabaseOutputStream(OutputStream outputStream) {
        super(outputStream);
    }

    /**
     * Записывает в БД в следующем формате:
     * - Размер ключа в байтах используя {@link WritableDatabaseRecord#getKeySize()}
     * - Ключ
     * - Размер записи в байтах {@link WritableDatabaseRecord#getValueSize()}
     * - Запись
     * Например при использовании UTF_8,
     * "key" : "value"
     * 3key5value
     * Метод вернет 10
     *
     * @param databaseRecord запись
     * @return размер записи
     * @throws IOException если запись не удалась
     */
    public int write(WritableDatabaseRecord databaseRecord) throws IOException {
        if (databaseRecord instanceof RemoveDatabaseRecord){
            writeInt(databaseRecord.getKeySize());
            write(databaseRecord.getKey());
            writeInt(-1);
        } else {
            writeInt(databaseRecord.getKeySize());
            write(databaseRecord.getKey());
            int valueSize = databaseRecord.getValueSize();
            if (valueSize < 1){
                writeInt(0);
            }
            else {
                writeInt(valueSize);
                write(databaseRecord.getValue());
            }
        }
        flush();
        return size();
    }
}
