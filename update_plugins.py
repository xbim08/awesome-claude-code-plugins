import os
import json

base_url = "https://github.com/dudley02/awesome-claude-code-plugins"

for root, _, files in os.walk("."):
    for file in files:
        if file == "plugin.json":
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                
                # 删除字段
                data.pop("keywords", None)
                data.pop("agents", None)
                data.pop("commands", None)
                data.pop("category", None)
                
                # 更新 homepage
                data["homepage"] = f"{base_url}/plugins/{data.get('name')}"

                # 写回文件
                with open(path, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                
                print(f"✅ Updated: {path}")
            except Exception as e:
                print(f"❌ Error updating {path}: {e}")
