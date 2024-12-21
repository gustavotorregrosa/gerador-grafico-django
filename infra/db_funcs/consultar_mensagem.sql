CREATE OR REPLACE FUNCTION consultar_mensagem(cliente_id INT)
RETURNS TABLE (
    mensagem_id INT,
    cliente_id INT,
    conteudo TEXT,
    data_envio TIMESTAMP
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        mensagem_id,
        cliente_id,
        conteudo,
        data_envio
    FROM 
        mensagens
    WHERE 
        cliente_id = consultar_mensagem.cliente_id;
END;
$$ LANGUAGE plpgsql;