package com.itmo.java.protocol;

import com.itmo.java.protocol.model.RespArray;
import com.itmo.java.protocol.model.RespBulkString;
import com.itmo.java.protocol.model.RespCommandId;
import com.itmo.java.protocol.model.RespError;
import com.itmo.java.protocol.model.RespObject;

import java.io.BufferedInputStream;
import java.io.DataInputStream;
import java.io.EOFException;
import java.io.IOException;
import java.io.InputStream;
import java.io.PushbackInputStream;

public class RespReader implements AutoCloseable {
    // TODO 1. заметил, что все классы наследующие InputStream не ставят @Override
    //  для его абстрактных методов. Поч?
    // TODO 2. есть условный метод peek чтобы сделать read и unread одновременно?
    // TODO 3. почему если Pushback записывает (unread) не сразу, а в буфер, то нет
    //  какого-нибудь flush()?
    private final PushbackInputStream pushbackStream;
    private final DataInputStream dataStream;

    /**
     * Специальные символы окончания элемента
     */
    private static final byte CR = '\r';
    private static final byte LF = '\n';
    public RespReader(InputStream is) {
        // TODO 200 iq код
        this.pushbackStream = new PushbackInputStream(new BufferedInputStream(is));
        this.dataStream = new DataInputStream(pushbackStream);
    }

    /**
     * Есть ли следующий массив в стриме?
     */
    public boolean hasArray() throws IOException {
        int singleChar = readSingleByte();
        pushbackStream.unread(singleChar);

        return (singleChar == RespArray.CODE);
    }

    // TODO уточнить бы что вернет RespError, а не "ошибку"
    /**
     * Считывает из input stream следующий объект. Может прочитать любой объект, сам определит его тип на основе кода объекта.
     * Например, если первый элемент "-", то вернет ошибку. Если "$" - bulk строку
     *
     * @throws EOFException если stream пустой
     * @throws IOException  при ошибке чтения
     */
    public RespObject readObject() throws IOException {
        int singleByte = readSingleByte();
        pushbackStream.unread(singleByte);

        switch (singleByte) {
            case RespError.CODE:
                return readError();
            case RespBulkString.CODE:
                return readBulkString();
            case RespArray.CODE:
                return readArray();
            case RespCommandId.CODE:
                return readCommandId();
            default:
                // TODO ПОЧЕМУ НИГДЕ НЕ СКАЗАНО ЧТО НУЖНО ЗАКРЫВАТЬ ЧТО-ТО?!?!?!?!?!?!!?!
                 close();
                throw new IOException("Can't define Resp type " + singleByte);
        }
    }

    /**
     * Считывает объект ошибки
     *
     * @throws EOFException если stream пустой
     * @throws IOException  при ошибке чтения
     */
    public RespError readError() throws IOException {
        checkType(RespError.CODE);

        return new RespError(readToCRLF().getBytes());
    }

    /**
     * Читает bulk строку
     *
     * @throws EOFException если stream пустой
     * @throws IOException  при ошибке чтения
     */
    public RespBulkString readBulkString() throws IOException {
        checkType(RespBulkString.CODE);

        int stringLen = Integer.parseInt(readToCRLF());

        if (stringLen == RespBulkString.NULL_STRING_SIZE) {
            return RespBulkString.NULL_STRING;
        }

        byte[] result = readNBytes(stringLen);
        readCRLF();

        return new RespBulkString(result);
    }

    /**
     * Считывает массив RESP элементов
     *
     * @throws EOFException если stream пустой
     * @throws IOException  при ошибке чтения
     */
    public RespArray readArray() throws IOException {
        checkType(RespArray.CODE);

        int elementsAmount = Integer.parseInt(readToCRLF());

        RespObject[] respObjects = new RespObject[elementsAmount];
        for (int i = 0; i < elementsAmount; i++) {
            respObjects[i] = readObject();
        }

        return new RespArray(respObjects);
    }

    /**
     * Считывает id команды
     *
     * @throws EOFException если stream пустой
     * @throws IOException  при ошибке чтения
     */
    public RespCommandId readCommandId() throws IOException {
        checkType(RespCommandId.CODE);

        RespCommandId result = new RespCommandId(dataStream.readInt());
        readCRLF();
        return result;
    }

    private String readToCRLF() throws IOException {
        StringBuilder stringBuilder = new StringBuilder();
        int newChar;
        boolean checker = false;

        while (true) {
            newChar = readSingleByte();

            if (checker && newChar == LF) {
                stringBuilder.setLength(Math.max(stringBuilder.length() - 1, 0)); // Удаляем \r
                return stringBuilder.toString();
            }

            stringBuilder.append((char) newChar);

            checker = newChar == CR;
        }
    }

    private byte readSingleByte() throws IOException {
        byte singleByte = (byte) pushbackStream.read();

        if (singleByte  == -1) {
            // TODO ПОЧЕМУ НИГДЕ НЕ СКАЗАНО ЧТО НУЖНО ЗАКРЫВАТЬ ЧТО-ТО?!?!?!?!?!?!!?! x2
            close();
            throw new EOFException("Unexpected end of stream!");
        }

        return singleByte;
    }

    private byte[] readNBytes(int len) throws IOException {
        // TODO почему is.read возвращает int (а не short или Optional<byte>), а readNBytes byte[]?
        byte[] bytes = pushbackStream.readNBytes(len);

        if (bytes.length != len) {
            throw new EOFException("Unexpected end of stream!");
        }

        return bytes;
    }

    private void readCRLF() throws IOException {
        int possibleCR = readSingleByte();
        int possibleLF = readSingleByte();

        if (possibleCR != CR || possibleLF != LF) {
            throw new IOException("Expected 1310 (<CR><LF>), but found " + possibleCR + possibleLF);
        }
    }

    private void checkType(byte expect) throws IOException {
        int a = readSingleByte();
        if (a != expect) {
            throw new IOException("Wrong type! Found " + a + " but expect " + expect);
        }
    }

    @Override
    public void close() throws IOException {
        dataStream.close();
        pushbackStream.close();
    }
}
