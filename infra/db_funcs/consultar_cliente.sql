CREATE OR REPLACE FUNCTION consultar_cliente(p_id INTEGER)
RETURNS TABLE(id INTEGER, nome VARCHAR, email VARCHAR, telefone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT id, nome, email, telefone
    FROM clientes
    WHERE id = p_id;
END;
$$ LANGUAGE plpgsql;