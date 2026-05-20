create or replace table `proyecto1.DATASET.tabla_meteo_dif` as
with datos_dia as (
    select
        town,
        cast(
            cast(time as datetime) as date
        ) as date,
        temp,
        wind,
        humidity
    from `proyecto1.DATASET.tabla_meteo`
    ),
    agregado_lugar_dia as (
    select
        town,
        date,
        max(temp) as max_temp
    from datos_dia
    group by town, date
    ),
    dia_anterior AS (
    select
        town,
        date,
        max_temp,
        lag(max_temp) over (
            partition by town
            order by date
        ) AS max_anterior
    from agregado_lugar_dia
    )
    select
        town,
        date,
        coalesce(max_temp - max_anterior, 0) as diferencia_temperatura_max
    from dia_anterior
    order by town, date
