CREATE OR REPLACE FUNCTION listar_mensagens()
RETURNS TABLE (
    id INT,
    texto TEXT,
    enviado_em TIMESTAMP,
    status TEXT,
    cliente_id INT
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        m.mensagem_id as id,
        m.conteudo as texto,
        m.status as status,
        m.data_envio as enviado_em,
        m.cliente_id as cliente_id,
       
    FROM 
        mensagens m
   
END;
$$ LANGUAGE plpgsql;