package com.itmo.java.basics.console;

import com.itmo.java.protocol.model.RespObject;

public interface DatabaseApiSerializable {
    /**
     * Возвращает представление данного объекта в RESP протоколе.
     *
     * @return представление данного объекта в RESP протоколе
     */
    RespObject serialize();
}
