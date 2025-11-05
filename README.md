# 🖼️ Remover Fundo API (Render)

API simples que usa `rembg` para remover o fundo de imagens, pronta para integrar com seu plugin WordPress.

---

## 🚀 Deploy no Render

1. Crie um novo repositório no GitHub (por exemplo `remover-fundo-api`).
2. Envie estes arquivos:
   - `main.py`
   - `requirements.txt`
   - `render.yaml`
   - `README.md`
3. Vá em [Render.com](https://render.com) → **New → Web Service**
4. Escolha seu repositório do GitHub.
5. Configure:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn main:app --bind 0.0.0.0:$PORT`
   - **Region:** a mais próxima do Brasil
6. (Opcional) Em **Environment Variables**, adicione:
   - `API_KEY` → sua senha (por ex: `minhachave123`)
7. Clique em **Deploy Web Service**

---

## 🧪 Teste

Use `curl` no terminal:

```bash
curl -X POST "https://seu-nome.onrender.com/remove-bg"   -F "file=@foto.jpg"   --output resultado.png
```

O arquivo `resultado.png` será a imagem com fundo transparente.

---

## 🔗 Integração com o WordPress

1. Vá em **Configurações → Remover Fundo Grátis**.
2. No campo “URL da API”, coloque:

```
https://seu-nome.onrender.com/remove-bg
```

3. Se tiver configurado uma `API_KEY`, adicione o cabeçalho:

```
Authorization: Bearer minhachave123
```

4. Crie uma página com o shortcode:

```
[remover_fundo_ia]
```

5. Teste o upload — o plugin enviará a imagem para o Render e mostrará o resultado.

---

## ✅ Pronto!

Agora seu plugin WordPress está conectado a uma API de remoção de fundo profissional rodando no Render.
