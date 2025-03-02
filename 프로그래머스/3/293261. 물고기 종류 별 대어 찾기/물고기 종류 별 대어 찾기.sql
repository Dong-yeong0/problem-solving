SELECT 
    fi.ID,
    fn.FISH_NAME,
    fi.LENGTH
FROM 
    FISH_INFO fi
JOIN 
    FISH_NAME_INFO fn 
ON 
    fi.FISH_TYPE = fn.FISH_TYPE
WHERE 
    fi.LENGTH IS NOT NULL 
AND
    fi.LENGTH = (
        SELECT 
            MAX(LENGTH)
        FROM 
            FISH_INFO
        WHERE 
            FISH_TYPE = fi.FISH_TYPE 
        AND 
            LENGTH IS NOT NULL
    )
ORDER BY 
    fi.ID ASC
