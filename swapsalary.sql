update salary set sex = CASE sex
    WHEN 'f' THEN 'm'
    ELSE 'f'
    end ;