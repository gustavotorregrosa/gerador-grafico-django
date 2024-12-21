CREATE OR REPLACE FUNCTION listar_clientes()
RETURNS TABLE(id INT, nome VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT clientes.id as id, clientes.nome as nome
    FROM clientes;
END;
$$ LANGUAGE plpgsql;