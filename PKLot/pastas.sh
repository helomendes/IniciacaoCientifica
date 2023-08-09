#!/bin/bash

DIR="/home/heloisa/Codigos/IC/PKLot/oficial"
NOVO="/home/heloisa/Codigos/IC/PKLot/oficial/Novo"

if [ ! -d ${NOVO} ]; then
    mkdir ${NOVO}
fi

IMAGENS="/home/heloisa/Downloads/PKLot/PKLotSegmented"
for ESTACIONAMENTO in $(ls ${IMAGENS});
do
    CLOUDY="${IMAGENS}/${ESTACIONAMENTO}/Cloudy"
    RAINY="${IMAGENS}/${ESTACIONAMENTO}/Rainy"
    SUNNY="${IMAGENS}/${ESTACIONAMENTO}/Sunny"
    
    if [ ! -d "${NOVO}/${ESTACIONAMENTO}" ]; then
        mkdir "${NOVO}/${ESTACIONAMENTO}"
    fi
    
    #Cloudy x Rainy e Cloudy x Sunny
    for DIA in $(ls ${CLOUDY});
    do
        #cira o novo diretorio do dia
        if [ ! -d "${NOVO}/${ESTACIONAMENTO}/${DIA}" ]; then
            mkdir "${NOVO}/${ESTACIONAMENTO}/${DIA}"
        fi
        if [ ! -d "${NOVO}/${ESTACIONAMENTO}/${DIA}/Empty" ]; then
            mkdir "${NOVO}/${ESTACIONAMENTO}/${DIA}/Empty"
        fi
        if [ ! -d "${NOVO}/${ESTACIONAMENTO}/${DIA}/Occupied" ]; then
            mkdir "${NOVO}/${ESTACIONAMENTO}/${DIA}/Occupied"
        fi

        #passa pro novo diretorio do dia
        for ARQUIVO in $(ls "${CLOUDY}/${DIA}/Empty");
        do
            cp "${CLOUDY}/${DIA}/Empty/${ARQUIVO}" "${NOVO}/${ESTACIONAMENTO}/${DIA}/Empty"
        done
        for ARQUIVO in $(ls "${CLOUDY}/${DIA}/Occupied");
        do
            cp "${CLOUDY}/${DIA}/Occupied/${ARQUIVO}" "${NOVO}/${ESTACIONAMENTO}/${DIA}/Occupied"
        done

        #junta com a chuva
        if [ -d "${RAINY}/${DIA}" ]; then
            for ARQUIVO in $(ls "${RAINY}/${DIA}/Empty");
            do
                cp "${RAINY}/${DIA}/Empty/${ARQUIVO}" "${NOVO}/${ESTACIONAMENTO}/${DIA}/Empty"
            done
            for ARQUIVO in $(ls "${RAINY}/${DIA}/Occupied");
            do
                cp "${RAINY}/${DIA}/Occupied/${ARQUIVO}" "${NOVO}/${ESTACIONAMENTO}/${DIA}/Occupied"
            done
        fi

        #junta com o sol
        if [ -d "${SUNNY}/${DIA}" ]; then
            for ARQUIVO in $(ls "${SUNNY}/${DIA}/Empty");
            do
                cp "${SUNNY}/${DIA}/Empty/${ARQUIVO}" "${NOVO}/${ESTACIONAMENTO}/${DIA}/Empty"
            done
            for ARQUIVO in $(ls "${SUNNY}/${DIA}/Occupied");
            do
                cp "${SUNNY}/${DIA}/Occupied/${ARQUIVO}" "${NOVO}/${ESTACIONAMENTO}/${DIA}/Occupied"
            done
        fi
    done

    for DIA in $(ls ${RAINY});
    do
        #cira o novo diretorio do dia
        if [ ! -d "${NOVO}/${ESTACIONAMENTO}/${DIA}" ]; then
            mkdir "${NOVO}/${ESTACIONAMENTO}/${DIA}"
        fi
        if [ ! -d "${NOVO}/${ESTACIONAMENTO}/${DIA}/Empty" ]; then
            mkdir "${NOVO}/${ESTACIONAMENTO}/${DIA}/Empty"
        fi
        if [ ! -d "${NOVO}/${ESTACIONAMENTO}/${DIA}/Occupied" ]; then
            mkdir "${NOVO}/${ESTACIONAMENTO}/${DIA}/Occupied"
        fi

        #passa pro novo diretorio do dia
        for ARQUIVO in $(ls "${RAINY}/${DIA}/Empty");
        do
            cp "${RAINY}/${DIA}/Empty/${ARQUIVO}" "${NOVO}/${ESTACIONAMENTO}/${DIA}/Empty"
        done
        for ARQUIVO in $(ls "${RAINY}/${DIA}/Occupied");
        do
            cp "${RAINY}/${DIA}/Occupied/${ARQUIVO}" "${NOVO}/${ESTACIONAMENTO}/${DIA}/Occupied"
        done

        #junta com o sol
        if [ -d "${SUNNY}/${DIA}" ]; then
            for ARQUIVO in $(ls "${SUNNY}/${DIA}/Empty");
            do
                cp "${SUNNY}/${DIA}/Empty/${ARQUIVO}" "${NOVO}/${ESTACIONAMENTO}/${DIA}/Empty"
            done
            for ARQUIVO in $(ls "${SUNNY}/${DIA}/Occupied");
            do
                cp "${SUNNY}/${DIA}/Occupied/${ARQUIVO}" "${NOVO}/${ESTACIONAMENTO}/${DIA}/Occupied"
            done
        fi
    done


    for DIA in $(ls ${SUNNY});
    do
        #cira o novo diretorio do dia
        if [ ! -d "${NOVO}/${ESTACIONAMENTO}/${DIA}" ]; then
            mkdir "${NOVO}/${ESTACIONAMENTO}/${DIA}"
        fi
        if [ ! -d "${NOVO}/${ESTACIONAMENTO}/${DIA}/Empty" ]; then
            mkdir "${NOVO}/${ESTACIONAMENTO}/${DIA}/Empty"
        fi
        if [ ! -d "${NOVO}/${ESTACIONAMENTO}/${DIA}/Occupied" ]; then
            mkdir "${NOVO}/${ESTACIONAMENTO}/${DIA}/Occupied"
        fi

        #passa pro novo diretorio do dia
        for ARQUIVO in $(ls "${SUNNY}/${DIA}/Empty");
        do
            cp "${SUNNY}/${DIA}/Empty/${ARQUIVO}" "${NOVO}/${ESTACIONAMENTO}/${DIA}/Empty"
        done
        for ARQUIVO in $(ls "${SUNNY}/${DIA}/Occupied");
        do
            cp "${SUNNY}/${DIA}/Occupied/${ARQUIVO}" "${NOVO}/${ESTACIONAMENTO}/${DIA}/Occupied"
        done
    done
done